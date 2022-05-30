var i= 1;
while (i < 4){
    var step = "";
    if (1 == 1){
        step = " step";
    }else{
        step = " steps";
    }
    console.log(i.toString() + step);
    i = i + 1
}
 // ne prend pas en conmpte le else, résultat toutjours "step" et jamais "steps"