import React from 'react'; 
import { Routes, Route, BrowserRouter } from 'react-router-dom'; 
import Home from './pages/Home'; 
import About from './pages/About'; 
import EnggNotes from './pages/EnggNotes'; 
import PharmNotes from './pages/PharmNotes'; 
import Contact from './pages/Contact'; 
import NoPage from './pages/NoPage'; 
export default function App(){ 
return( 
<BrowserRouter> 
      <Routes> 
         <Route path='/' element={<Home />} /> 
         <Route path='/about' element={<About />} /> 
         <Route path='/enggnotes' element={<EnggNotes />} /> 
         <Route path='/pharmnotes' element={<PharmNotes />} /> 
         <Route path='/contact' element={<Contact />} /> 
         <Route path='*' element={<NoPage />} /> 
       </Routes> 
 </BrowserRouter> 
 ) 
 }