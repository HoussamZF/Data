

function majTab(etatCourant){
    console.log("CALL majTab");    
    lanceFetchDataJoueursEtInsereData(etatCourant);
}


function majPage(etatCourant){
    console.log("CALL majPage");
    majTab(etatCourant);
}


function initClientJoueurs(){
    console.log("CALL initClientJoueurs");
    const etatInitial = {
        joueur: null,
        joueurChoisiRang: 0,
        tabJoueurs : null,
        tabJoueursSortedBy : "VM",
        tabJoueursTaillePage: 1,
        tabJoueursNumeroPage: 10
    };
    majPage(etatInitial);
}


initClientJoueurs();