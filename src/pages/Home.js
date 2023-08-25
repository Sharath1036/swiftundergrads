import React from "react";
import "../App.css";
import "../responsive.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import Service from "../components/Service";
import Testimonials from '../components/Testimonials';

export default function Home() {
  return (
    <div class="App">
      <div class="container-fluid bg1">
      <Navbar />
        <br /><br /><br /><br /><br /><br />
        <div class="jumbotron bg-transparent font1">
          <h1>Swift <span class="text-danger">U</span>nder<span class="text-danger">G</span>rads</h1>
          <p>Your guide to MHT-CET</p>
        </div>
      </div>

      <div class="jumbotron bg2 para1">
        <div>विद्याधनं सर्व धनं प्रधानम्</div>
      </div>
      <br />

      <h3 class="arial">OUR SERVICES</h3>
      <br /><br />
      <Service />
      <br/> <br/>

      <div class="container">
      <h3 class="mb-5 arial">TESTIMONIALS</h3>
      <Testimonials />
      </div>  

      <hr/>

      <div class="mb-5">
      <h3 class="mb-5 arial">OUR SOCIALS</h3>
      <div class="socials"><a href="mailto:swiftundergrads@gmail.com"><img alt="gmail" class="icons" src={require("../images/gmail.webp")} /></a></div>
      <div class="socials"><a href="https://www.github.com/Sharath1036/"><img alt="instagram" class="icons" src={require("../images/instagram.png")} /></a></div>
      <div class="socials"><a href="https://www.behance.net/sharathp2/"><img alt="linkedin" class="icons" src={require("../images/linkedin.png")} /></a></div>
      <div class="socials"><a href="https://www.linkedin.com/in/sharathpai107"><img alt="telegram" class="icons" src={require("../images/telegram.webp")} /></a></div>
      </div>

      <div ><Footer /></div>
    </div>
  );
}
