/**
 * forme une entete dans un tableau HTML
 * @param {string} dataEnTete 
 * @returns 
 */
function creationCase(dataCase){
    return '<th>' + dataCase + '</th>'
}

/**
 *  forme une ligne d'un tableau en HTML
 * @param {string} dataUnLigne 
 */
function creationUneLigne(dataUneLigne){
    return '<tr>' + dataUneLigne + '</tr>';
}

/**
 *  forme le tableau en HTML on va afficher pour l'instant seulement les données importantes dans notre tableau
 * @param {object[]} data 
 * @returns 
 */
function creationTabClubs(data){

    let textHTML = '';

    for(let i=0; i<10; i++){ // 2653 la taille du tableau on veut aller de 10 en 10 en appuyant sur un bouton
        textHTML = textHTML + creationCase("<img src=" + data[i].photo + ">") + "\n"
                            + creationCase(data[i].nomClub) + "\n"
                            + creationCase(data[i].effectifTaille) + "\n"
                            + creationCase(data[i].bilanTransfert) + "\n"
                            + creationCase(data[i].nbJoueurEtrangers) + "\n"
                            + creationCase(data[i].prcntJoueurEtrangers) + "\n"
                            + creationCase(data[i].nomStade) + "\n"
                            + creationCase(data[i].ageMoyen) + "\n"
                            + creationCase(data[i].valeurMarchande) + "\n";
                            

        textHTML = creationUneLigne(textHTML);
    }
    
    return textHTML;
}

/**
 * coté server
 * @returns 
 */
function fetchDataClubs(){
    return fetch('http://lif.sci-web.net/~datatransfert/Clubs.json')
        .then((reponse) => {
            return reponse.json();
        })
        .then((data) =>{
            return data;
        });
}

function lanceFetchDataClubsEtInsereData(etatCourant){
    console.log('CALL lanceFetchDataClubsEtInsereData');

    return fetchDataClubs()
        .then((data) => {
            const divTag = document.getElementById("div-data-clubs");
            etatCourant.tabClubs = data;
            divTag.innerHTML = creationTabClubs(etatCourant.tabClubs);
        })
}



