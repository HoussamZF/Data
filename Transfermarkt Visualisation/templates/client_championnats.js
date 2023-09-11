

function majTab(etatCourant){
    console.log("CALL majTab");    
    lanceFetchDataChampionnatsEtInsereData(etatCourant);
}


function majPage(etatCourant){
    console.log("CALL majPage");
    majTab(etatCourant);
}


function initClientChampionnats(){
    console.log("CALL initClientJoueurs");
    const etatInitial = {
        tabChampionnat : null
    };
    majPage(etatInitial);
}


initClientChampionnats();
