function checkCashRegister(price, cash, cid) {
  const amnt = {
    "PENNY": .01,
    "NICKEL": .05,
    "DIME": .10,
    "QUARTER": .25,
    "ONE": 1.00,
    "FIVE": 5.00,
    "TEN": 10.00,
    "TWENTY": 20.00,
    "ONE HUNDRED": 100.00
  }
  let totalCid = 0,i;
  for ( i of cid) {
    totalCid += i[1];
  }
  totalCid = totalCid.toFixed(2);
  let change = cash - price;
  const changeArray = [];
  if (change > totalCid) {
    return { status: "INSUFFICIENT_FUNDS", change: changeArray };
  } else if (change.toFixed(2) === totalCid) {
    return { status: "CLOSED", change: cid };
  } else {
    cid = cid.reverse();
    for (i of cid) {
      let temp = [i[0], 0];
      while (change >= amnt[i[0]] && i[1] > 0) {
        temp[1] += amnt[i[0]];
        i[1] -= amnt[i[0]];
        change -= amnt[i[0]];
        change = change.toFixed(2);
      }
      if (temp[1] > 0) {
        changeArray.push(temp);
      }
    }
  }
  if (change > 0) {
    return { status: "INSUFFICIENT_FUNDS", change: [] };
  }
  return { status: "OPEN", change: changeArray};
}

console.log(checkCashRegister(19.5, 20, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 1], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]) 
)