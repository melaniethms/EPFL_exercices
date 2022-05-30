class ImprimanteTroisD{
    constructor (name, type){
        this.name = name
        this.type = type
    }
        testPrint() {
            console.log(`${this.name} print a boat for testing`);
        }
        buseBouchée(){
            console.log(`Oh non !! La buse de ${this.name} est bouchée, l'impression a échoué !`);
        }
}

const UltimakerTrois = new ImprimanteTroisD("ultimaker 3", "FDM");
const PrusaMkTrois = new ImprimanteTroisD("prusa MK3", "FDM");
const PrusaSlUn = new ImprimanteTroisD("Prusa SL1", "SLA");

UltimakerTrois.testPrint();
console.log(`${PrusaSlUn.name} is a ${PrusaSlUn.type} printer`);
console.log(PrusaMkTrois.name + " is a " + PrusaMkTrois.type + " printer");
PrusaMkTrois.buseBouchée();