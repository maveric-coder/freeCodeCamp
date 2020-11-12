function rot13(str) {
  var ls='',i,n=0;
  for (i=0;i<str.length;i+=1){
    
    if (str[i].match("^[A-Z]*$")){
      
      n=str.charCodeAt(i)
      
      if (n>=78){
        
        ls+=String.fromCharCode(n-13)
      }
      else{
        n=90-77+n
        ls+=String.fromCharCode(n)

      }


    }
    else{

      ls+=str[i]
    }

  }
  
  return ls;
}

console.log(rot13("SERR PBQR PNZC"));
