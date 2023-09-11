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
function creationTabChampionnats(data){

    let textHTML = '';

    for(let i=0; i<5; i++){ // 2653 la taille du tableau on veut aller de 10 en 10 en appuyant sur un bouton
        textHTML = textHTML + creationCase("<img src=" + data[i].photo + ">") + "\n"
                            + creationCase(data[i].nom) + "\n"
                            + creationCase(data[i].taille) + "\n"
                            + creationCase(data[i].nbJoueurs) + "\n"
                            + creationCase(data[i].nbJoueursEtrangers) + "\n"
                            + creationCase(data[i].prcntJoueursEtrangers) + "\n"
                            + creationCase(data[i].ageMoyen) + "\n"
                            + creationCase(data[i].meilleurJoueur) + "\n"
                            + creationCase(data[i].valeurMarchande) + "\n";

        textHTML = creationUneLigne(textHTML);
    }
    
    return textHTML;
}

/**
 * coté server
 * @returns 
 */
function fetchDataChampionnants(){
    return fetch('./tst')
        .then((reponse) => {
            return reponse.json();
        })
        .then((data) =>{
            return data;
        });
}

function lanceFetchDataChampionnatsEtInsereData(etatCourant){
    console.log('CALL lanceFetchDataJoueursEtInsereData');

    return fetchDataChampionnants()
        .then((data) => {
            const divTag = document.getElementById("div-data-championnats");
            etatCourant.tabChampionnat = data;
            divTag.innerHTML = creationTabChampionnats(etatCourant.tabChampionnat);
        })
}



