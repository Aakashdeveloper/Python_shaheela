const Bus = function(color){
    this.color = color;
}

Bus.prototype = {
    getColor(){
        return this.color
    }
};

const ToyCar = function(){

}

ToyCar.prototype = Object.create(Bus.prototype)

const legoCar = new ToyCar()