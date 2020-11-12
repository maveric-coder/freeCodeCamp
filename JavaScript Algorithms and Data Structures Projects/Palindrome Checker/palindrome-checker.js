function palindrome(str) {

  var n = str.length;
  var st=[];
  var i=0,j=0;
  
  while (i<n){
    if (str[i].match("^[a-zA-Z0-9]*$")){
          st[j]=str[i].toLowerCase();
          j+=1
    }
    i+=1

  }
  n=st.length;
  j=n-1
  n=Math.round(n/2);
  i=0

  while (i<n){
    if (st[i]!=st[j]){
      return false

    }
    i+=1
    j-=1

  }

  
  return true;
}



palindrome("My age is 0, 0 si ega ym.");
