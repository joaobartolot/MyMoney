function getCurrencyText(amount) {
  if (amount == 0) return "R$ 0,00";

  let text = amount.toString();

  if (text.length == 1) return "R$ 0,0" + text;
  else if (text.length == 2) return "R$ 0," + text;
  else return "R$ " + text.slice(0, -2) + "," + text.slice(-2);
}
