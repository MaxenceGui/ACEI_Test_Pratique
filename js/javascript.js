
const addPlayerToBD = () =>{

    let url = document.getElementsByClassName("url_entry")[0].value;
    console.log(url)

    formData = new FormData();
    formData.append("url", url);
    
    fetch("http://127.0.0.1:5000/add_players",
    {
        method: 'POST',
        body: formData
    })

}