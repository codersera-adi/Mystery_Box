fetch("https://api.quotable.io/random")
  .then(res => res.json())
  .then(data => console.log(data));
