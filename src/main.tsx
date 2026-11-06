import {createRoot} from 'react-dom/client';
import {Scene} from './BaselineScene';
import {ShelbyScene} from './ShelbyScene';
import './shell.css';
const baseline=new URLSearchParams(location.search).has('baseline');
createRoot(document.getElementById('root')!).render(baseline?<Scene/>:<ShelbyScene/>);
