import Component from "@glimmer/component/dist/types/src/component";

export default class App extends Component {
    //@tracked
    _instance = [ 'deal damage' ];

    get instance(){
        return this._instance;
    }
}