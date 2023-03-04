console.log("im here")
showtask()
var  mytask = document.getElementById('mytask')
// ------------------------CSRF token  ----------------------------
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');  

// ------------------------show data ----------------------------
function showtask(){
        console.log("im clicked ")

        fetch('http://127.0.0.1:8000/api')
        .then((res) => res.json())
        .then(function(data){
            console.log(data)
            var list= data.Paylod
            for (var i in list){
                console.log(list[i].title)
                var item =`

                <tr>
                <td>${list[i].title} </td>
        
                <td> ${list[i].completed}</td>
                <td> <button type="button" class="btn btn-danger" onclick= deletedata(${list[i].id})>Delete</button> </td>
              </tr>


            `

                mytask.innerHTML = mytask.innerHTML + item
            }
        })
}
// ------------------------checkbox ----------------------------

function checkbox(){
    var checkbox = document.getElementById('checkbox1').value
    console.log(checkbox)
    if (checkbox.checked == true){
        alert("work done")
      } else {
        alert("not tik");
      }

}

// ------------------------delete ----------------------------

function deletedata(item){
    console.log("hiiiiiidlete")
    alert(item)
    var url = 'http://127.0.0.1:8000/api/taskdelete/'+item
    fetch(url,{
        method:'DELETE',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken': csrftoken,
            }
        }).then((res)=>{
            location.reload();
        })

        
}

// ------------------------ ADd Item  ----------------------------
function Taskdata(){

    var mytaskname =document.getElementById('mytaskname').value;
    console.log(mytaskname)

    var url = 'http://127.0.0.1:8000/api/taskadd/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken': csrftoken,
                },
        body:JSON.stringify({'title':mytaskname})
    })
    .then(function(res){
        location.reload();
    })
}
