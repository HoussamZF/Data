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
function creationTabJoueurs(data){

    let textHTML = '';

    for(let i=2124; i<2134; i++){ // 2653 la taille du tableau on veut aller de 10 en 10 en appuyant sur un bouton
        textHTML = textHTML + creationCase("<img src=" + data[i].dataJoueur.photo + ">") + "\n"
                            + creationCase(data[i].dataJoueur.nom) + "\n"  
                            + creationCase(data[i].dataJoueur.nationalite) + "\n" 
                            + creationCase(data[i].dataJoueur.club) + "\n" 
                            + creationCase(data[i].dataJoueur.position) + "\n" 
                            + creationCase(data[i].dataJoueur.age) + "\n" 
                            + creationCase(data[i].dataJoueur.valeurMarchande) + "\n";

        textHTML = creationUneLigne(textHTML);
    }
    
    return textHTML;
}

function performanceJoueur(data){

    let textHTML = `<table class="table">
	<thead>
		<tr>
            <th>nomCompet</th>
            <th>nbMatch</th>
            <th>nbBut</th>
            <th>nbPasseD</th>
            <th>nbCartonJaune</th>
            <th>nbDoubleCartonJaune</th>
            <th>nbRouge</th>
            <th>nbTempsDeJeu</th>
		</tr>
	</thead>
	<tbody>`;
    console.log(data);

    for(let i in data){ 
        textHTML = textHTML + creationCase(data[i].nomCompet) + "\n" 
                            + creationCase(data[i].nbMatch) + "\n" 
                            + creationCase(data[i].nbBut) + "\n" 
                            + creationCase(data[i].nbPasseD) + "\n" 
                            + creationCase(data[i].nbCartonJaune) + "\n" 
                            + creationCase(data[i].nbDoubleCartonJaune) + "\n" 
                            + creationCase(data[i].nbRouge) + "\n" 
                            + creationCase(data[i].nbTempsDeJeu) + "\n"; 

        textHTML = creationUneLigne(textHTML);
    }
    console.log(textHTML);
    
    return textHTML + "	</tbody></table>";
}

function historiqueJoueur(data){

    let textHTML = `<table class="table">
	<thead>
		<tr>
            <th>saison</th>
            <th>date</th>
            <th>vendeur</th>
            <th>acheteur</th>
            <th>valeurMarchande</th>
            <th>montant</th>
		</tr>
	</thead>
	<tbody>`;
    console.log(data[0].valeurMarchande)

    for(let i in data){ 
        textHTML = textHTML + creationCase(data[i].saison) + "\n"
                            + creationCase(data[i].date) + "\n"  
                            + creationCase(data[i].vendeur) + "\n" 
                            + creationCase(data[i].acheteur) + "\n" 
                            + creationCase(data[i].valeurMarchande) + "\n" 
                            + creationCase(data[i].montant) + "\n";

        textHTML = creationUneLigne(textHTML);
    }
    
    return textHTML + "	</tbody></table>";
}

function joueurProfilHTML(dataCase){
    return `
    <div>
    <button class="close-btn">&times;</button>
    <div>
        <div>
            <div>
                <div>
                    <img src="${dataCase.dataJoueur.photo}">
                </div>
                <div>
                    <div>
                        <h3>${dataCase.dataJoueur.nom}</h3>
                        <span>${dataCase.dataJoueur.club}</span>
                    </div>
                    <ul>
                        <li><span>Date de naissance: </span>${dataCase.dataJoueur.dateDeNaissance}</li>
                        <li><span>Lieu de naissance: </span>${dataCase.dataJoueur.lieuDeNaissance}</li>
                        <li><span>Âge: </span>${dataCase.dataJoueur.age}</li>
                        <li><span>Taille: </span>${dataCase.dataJoueur.taille}</li>
                        <li><span>Nationnalité: </span>${dataCase.dataJoueur.nationalite}</li>
                        <li><span>Poste: </span>${dataCase.dataJoueur.position}</li>
                        <li><span>Bon pied: </span>${dataCase.dataJoueur.bonPied}</li>
                        <li><span>Agent du joueur: </span>${dataCase.dataJoueur.agentDuJoueur}</li>
                        <li><span>Debut de contrat: </span>${dataCase.dataJoueur.debutContrat}</li>
                        <li><span>Fin de contrat: </span>${dataCase.dataJoueur.finContrat}</li>
                        <li><span>Option dans le contrat: </span>${dataCase.dataJoueur.optionContrat}</li>
                        <li><span>Equipementier: </span>${dataCase.dataJoueur.equipementier}</li>
                        <li><span>Valeur marchande: </span>${dataCase.dataJoueur.valeurMarchande}</li>
                    </ul>
                </div>
            </div>
            `+performanceJoueur(dataCase.PerformanceJoueur)+`
        </div>
        `+historiqueJoueur(dataCase.HistoriqueJoueur.tabTransfert)+`
    </div>
</div>
    `;
}

/**
 * 
 * @param {*} data 
 */
function JoueurSelectionne(etatCourant){
        let joueurChoisi = etatCourant.tabJoueurs[etatCourant.joueurChoisiRang];

        document.getElementById("joueur-selectionne").innerHTML = joueurProfilHTML(joueurChoisi);
}

/**
 * coté server
 * @returns 
 */
function fetchDataJoueurs(){
    return fetch('http://lif.sci-web.net/~datatransfert/Joueurs.json')
        .then((reponse) => {
            return reponse.json();
        })
        .then((data) =>{
            return data;
        });
}

function lanceFetchDataJoueursEtInsereData(etatCourant){
    console.log('CALL lanceFetchDataJoueursEtInsereData');

    return fetchDataJoueurs()
        .then((data) => {
            const divTag = document.getElementById("div-data-joueurs");
            etatCourant.tabJoueurs = data;
            divTag.innerHTML = creationTabJoueurs(etatCourant.tabJoueurs);
            JoueurSelectionne(etatCourant);
        })
}

// TODO 
function sortByValeurMarchande(etatCourant){
    const divTag = document.getElementById("div-data-joueurs");
}


