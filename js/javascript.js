const fetch_players = () =>{
    fetch("http://127.0.0.1:5000/fetch_players", {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(response=> {
        
        for(let i = 0; i < response.length; i++){
            let div = document.createElement("div")
            let player = ""
            for(let j = 0; j < response[i].length; j++){
                if( j !=0 ){
                    player += response[i][j] + " "
                }
            }
            div.innerHTML = player
            document.getElementsByClassName("table")[0].appendChild(div)
        }
    })
}

const addPlayerToBD = () =>{

    const player = []

    let entrys = document.getElementsByClassName("entry");
    
    for (let i = 0; i < entrys.length; i++){
        player.push(entrys[i].value)
    }

    data = {"player": player}
    console.log(data)

    const options = {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json'
        },
        body : JSON.stringify(player),
        //mode : 'no-cors'
    }
    
    fetch("http://127.0.0.1:5000/add_players", options)
    .then(response => response.json())
    .then(response =>{
        console.log(response);
    });
}