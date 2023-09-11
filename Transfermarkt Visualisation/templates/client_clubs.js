

function majTab(etatCourant){
    console.log("CALL majTab");    
    lanceFetchDataClubsEtInsereData(etatCourant);
}


function majPage(etatCourant){
    console.log("CALL majPage");
    majTab(etatCourant);
}


function initClientClubs(){
    console.log("CALL initClientJoueurs");
    const etatInitial = {
        tabClubs : null
    };
    majPage(etatInitial);
}


initClientClubs();
