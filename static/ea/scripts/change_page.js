


class Change_page{
    constructor(){
        this.DOM = {};
        this.DOM.main = document.querySelector('.main_info');
        this.DOM.backtest = document.querySelector('.back');
        this.DOM.fowardtest = document.querySelector('.foward');
        this.DOM.ea= document.querySelector('#ea');



        // this.DOM.container = document.querySelector('#global-container');
        this.eventType = this._getEventType();
        this._Event();
    }
    _getEventType() {
        return window.ontouchstart ? 'touchstart' : 'click'; 
    }
    // _add_back() {
    //     this.DOM.ea.classList.add('open-backtest');
    // }
    // _add_foward() {
    //     this.DOM.ea.classList.add('open-fowardtest');
    // }
    // _remove_back() {
    //     this.DOM.ea.classList.remove('open-backtest');
    // }
    // _remove_foward() {
    //     this.DOM.ea.classList.remove('open-fowardtest');
    // }

    _Event() {
        this.DOM.fowardtest.addEventListener(this.eventType, () => {
            if(this.DOM.ea.classList.contains('open-backtest')){
                this.DOM.ea.classList.remove('open-backtest');
                this.DOM.ea.classList.add('open-fowardtest');

                 
            }
            else{
                this.DOM.ea.classList.add('open-fowardtest');

            }
        }
        );
        
        this.DOM.backtest.addEventListener(this.eventType, () => {
            if(this.DOM.ea.classList.contains('open-fowardtest')){
                this.DOM.ea.classList.remove('open-fowardtest');
                this.DOM.ea.classList.add('open-backtest');

            }
            else{

                this.DOM.ea.classList.add('open-backtest');

            }
        }
        );

        this.DOM.main.addEventListener(this.eventType, () => {
            if(this.DOM.ea.classList.contains('open-backtest')){
                this.DOM.ea.classList.remove('open-backtest');

            }
            if(this.DOM.ea.classList.contains('open-fowardtest')){
                this.DOM.ea.classList.remove('open-fowardtest');
                
           }
            else{

            
            }
        }
    );
}
}
new Change_page();
