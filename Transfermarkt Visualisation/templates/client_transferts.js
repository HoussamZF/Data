

function majTab(etatCourant){
    console.log("CALL majTab");    
    lanceFetchDataTransfertsEtInsereData(etatCourant);
}


function majPage(etatCourant){
    console.log("CALL majPage");
    majTab(etatCourant);
}


function initClientTransferts(){
    console.log("CALL initClientJoueurs");
    const etatInitial = {
        tabTransferts : null
    };
    majPage(etatInitial);
}


initClientTransferts();
