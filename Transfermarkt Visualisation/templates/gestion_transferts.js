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
function creationTabTransferts(data){

    let textHTML = '';

    for(let i=0; i<10; i++){ // 964 la taille du tableau on veut aller de 10 en 10 en appuyant sur un bouton
        textHTML = textHTML + creationCase(data[i].nomJoueur) + "\n"
                            + creationCase(data[i].nomClubAcheteur) + "\n"
                            + creationCase(data[i].nomClubVendeur) + "\n"
                            + creationCase(data[i].prix) + "\n";
         

        textHTML = creationUneLigne(textHTML);
    }
    
    return textHTML;
}

/**
 * coté server
 * @returns 
 */
function fetchDataTransferts(){
    console.log('CALL fetchDataTransferts');
    return fetch('http://lif.sci-web.net/~datatransfert/Transferts.json')
        .then((reponse) => {
            return reponse.json();
        })
        .then((data) =>{
            return data;
        });
}

function lanceFetchDataTransfertsEtInsereData(etatCourant){
    console.log('CALL lanceFetchDataTransfertsEtInsereData');

    return fetchDataTransferts()
        .then((data) => {
            const divTag = document.getElementById("div-data-transferts");
            etatCourant.tabTransferts = data;
            divTag.innerHTML = creationTabTransferts(etatCourant.tabTransferts);
        })
}



