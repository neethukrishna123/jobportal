$(document).ready(function(){
    console.log("loaded")
    $('#register').click(function(){
        console.log("workedd")
       
        var fullname=$('#fname').val()
        console.log(fullname)
        
        if(fullname==""){
           
        
            $('#p1').show()
            return false
        }
    })  
})