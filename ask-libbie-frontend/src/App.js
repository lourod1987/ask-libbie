import React, { Component } from 'react';
// import logo from './logo.svg';
import { load_google_maps } from './GoogleMapsUtility'
import Map from './Map';
import Header from './Header';
import Sidebar from './Sidebar';
import './App.css';

class App extends Component {
    state = {
        query: '',
        locations: [],
        menu: false
    }

    componentDidMount() {
        let googleMapsPromise = load_google_maps();
        
        Promise.all([
            googleMapsPromise
        ])
        .then( values => {
            let google = values[0];
            
            this.google = google;
            this.markers = [];

            this.map = new google.maps.Map(document.getElementById('map'), {
                zoom: 10,
                center: {lat: 29.760427, lng: -95.369803},
                scrollwheel: true
            });   
            
        })
        .catch( () => {
            //alerts user if promise fails for any of the promises
            alert('One or more resources could not be retrieved. This app will not be fully functional until all network resources are successfully retrieved.');
        });

    }

     //show or hide the menu
    toggleMenu = () => {
        const map = document.getElementById('map');
        
        //add and remove classes that style the map according to whether or not the menu is displayed
        if (this.state.menu === true) {
            map.classList.remove('map-sidebar');
            map.classList.add('map');
        } else {
            map.classList.remove('map');
            map.classList.add('map-sidebar');
        }

        //change state of filterMenu boolean based on it's current state which toggles menu rendering
        return this.state.menu === true ?
            this.setState({ menu: false }) :
            this.setState({ menu: true });
    }

    render() {
        const { query, menu } = this.state;
        return (
            <div className="App">
                {/* <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
                </header> */}
                <Header toggleMenu={this.toggleMenu} />
                <main>
                    <Map />
                    { menu === true &&
                        <Sidebar
                            query={query}
                            // filter={ evt => {this.filter(evt.target.value)} }
                            // filteredPlaces={filteredPlaces}
                            // listSelect={this.listSelect}
                        />
                    }
                </main>
            </div>
        );
    }
}

export default App;
