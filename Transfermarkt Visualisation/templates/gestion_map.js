async function getData() {
    //recuperation des données du .json
    const response = await fetch('./Championnats');
    const data = await response.json();

    //ajout des championnats
    for (var i = 0; i < data.length; i++) {
        var {nom, tabEquipes} = data[i];

        var opt = document.createElement("option");
        opt.text = nom;
        opt.value = nom;
        document.getElementById("Championnats").options.add(opt);
    }
}

getData();

async function MajEquipes() {
    var leagues = document.getElementById('Championnats')
    var clubs = document.getElementById('Clubs')
    clubs.innerHTML = "";

    //
    const response = await fetch('./Championnats');
    const data = await response.json();

    var selectedLeague = leagues.options[leagues.selectedIndex].text;

    for (var i = 0; i < data.length; i++) {
        if(data[i].nom == selectedLeague) {
            for(var j = 0; j < data[i].tabEquipes.length; j++) {
                var equipe = data[i].tabEquipes[j];
                
                var opt = document.createElement("option");
                opt.text = equipe;
                opt.value = equipe;
                document.getElementById("Clubs").options.add(opt); 
            }
        }
    }
}