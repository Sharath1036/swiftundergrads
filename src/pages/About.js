import React from "react";
import "../App.css";
import "../responsive.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function About() {
  return (
    <div class="App">
      <div class="container-fluid bg4">
        <Navbar />
        <br /><br /><br /><br /><br /><br /><br/>
        <div class="jumbotron bg-transparent align-items-center mx-auto d-block">
          <h1>About Us</h1>
        </div>
      </div>

      <div class="jumbotron bg-transparent bg2 para1">
        <div class="container"><p class="lead">Swift Undergrads is a team comprising of undergraduate students conducting mentorship programs for students appearing for MHT-CET entrance exam. It provides services such as notes, quizzes, doubt solving, admission procedure guidance and many more.</p></div>
      </div>
      <br />

      <h3 class="mb-5 arial">MEET OUR TEAM</h3>
      <div class="container-fluid">
        <div class="row">
        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="sharath" class="mx-auto d-flex" src={require("../images/Sharath.jpg")}  width="300" height="300" />
          <br/>
          <h3>SHARATH PAI</h3>
          <p>FOUNDER | TECH LEAD</p>
          <div>
             <div class="socials"><a href="https://linkedin.com/in/sharathpai107"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://twitter.com/Sharath1072"><img alt="image" class="icons" src={require("../images/twitter.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/sharath_1007"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
              <div class="socials"><a href="https://github.com/Sharath1036"><img alt="github" class="icons" src={require("../images/github.webp")}  /></a></div>
        <br/><br/>
          </div>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Karan.jpg")}  width="300" height="300" />
          <br/>
          <h3>KARAN CHAVAN</h3>
          <p>ADMIN</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/karan-chavan-66b273222"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://twitter.com/Karanch66992447"><img alt="" class="icons" src={require("../images/twitter.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/karanchavan0503/"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Shreyas.jpeg")}  width="300" height="300" />
          <br/>
          <h3>SHREYAS GOSAVI</h3>
          <p>TREASURER</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/shreyas-gosavi-31b161215/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://twitter.com/SSG482"><img alt="image" class="icons" src={require("../images/twitter.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/ssg_482"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

          <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Chinmay.jpg")}  width="300" height="300" />
          <br/>
          <h3>CHINMAY DALAL</h3>
          <p>MARKETING LEAD</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/chinmay-dalal-79774b237/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/chinmay_0662"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Vaishnavi.jpg")}  width="300" height="300" />
          <br/>
          <h3>VAISHNAVI DESHMUKH</h3>
          <p>ENGINEERING TEAM MEMBER</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/vaishnavi-deshmukh-a84329230/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/vaishnavid3112/"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Shubham.jpeg")}  width="300" height="300" />
          <br/>
          <h3>SHUBHAM BANDGAR</h3>
          <p>ENGINEERING TEAM MEMBER</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/shubham-bandgar-00b531209/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
             <div class="socials"><a href="https://instagram.com/shubham_bandgar123"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Sayali.jpg")} width="300" height="300" />
          <br/>
          <h3>SAYALI SHIVPUJE</h3>
          <p>ENGINEERING TEAM MEMBER</p>
         <div class="align-items-center">
         <div class="socials"><a href="https://linkedin.com/in/sayali-s-58a83b236/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
          <div class="socials"><a href="https://instagram.com/saylii.58"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Harshal.jpg")} width="300" height="300" />
          <br/>
          <h3>HEMANT CHAUDHARI</h3>
          <p>PHARMACY TEAM MEMBER</p>
         <div class="align-items-center">
            <div class="socials"><a href="https://instagram.com/h.chaudhari_2004/"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Hemant.jpg")} width="300" height="300" />
          <br/>
          <h3>HARSHAL CHOPKAR</h3>
          <p>PHARMACY TEAM MEMBER</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/harshal-chopkar-711513251/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/harshalchopkar234"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Vaibhav.jpg")} width="300" height="300" />
          <br/>
          <h3>VAIBHAV NANDEKAR</h3>
          <p>PHARMACY TEAM MEMBER</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/vaibhav-nandekar-87a805214/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
             <div class="socials"><a href="https://instagram.com/nandekarv"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Rushikesh.jpg")} width="300" height="300" />
          <br/>
          <h3>RUSHIKESH MALI</h3>
          <p>AGRICULTURE TEAM MEMBER</p>
         <div class="align-items-center">
            <div class="socials"><a href="https://instagram.com/malirushikesh1032"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>

        <div class="col-lg-6 card cards bg-transparent border-0">
          <img alt="shreyas" class="mx-auto d-flex" src={require("../images/Jayesh.jpg")} width="300" height="300" />
          <br/>
          <h3>JAYESH WAGHODE</h3>
          <p>GRAPHIC DESIGNER</p>
         <div class="align-items-center">
             <div class="socials"><a href="https://linkedin.com/in/"><img alt="image" class="icons" src={require("../images/linkedin.png")}  /></a></div>
              <div class="socials"><a href="https://instagram.com/_yashh_07_"><img alt="instagram" class="icons" src={require("../images/instagram.png")}  /></a></div>
          </div>
        <br/><br/>
        </div>


        </div>
      </div>
      <div ><Footer /></div>

    </div>
  );
}
