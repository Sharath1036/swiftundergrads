import React from 'react';
import '../App.css';
import "../responsive.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function PharmNotes () {
    return(
        <div class="App">
      <Navbar />
      <div class="container-fluid bg6">
        <br /><br /><br /><br /><br /><br />
        <div class="jumbotron bg-transparent align-items-center mx-auto d-block">
          <h1>Pharmacy Notes</h1>
        </div>
        </div>

        <br /><br /><br />

        <div class="container-fluid">
      <div class="row">
          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/pharmaceutics1.webp")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">PHARMACEUTICS-I</h5>
                <p>NIRALI PRAKASHAN</p>
                <a href="https://drive.google.com/file/d/1dzDceVMkhPKLptUb0c-IQZNscPvZfZgL/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/phAnalysis.jpeg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">PHARMACEUTICAL ANALYSIS</h5>
                <p>NIRALI PRAKASHAN</p>
                <a href="https://drive.google.com/file/d/1eAZdi3dqzHD7YGx7sU8nBDCZfndYOGyC/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/hap1.jpeg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">HUMAN ANATOMY & PHYSIOLOGY-I</h5>
                <p>NIRALI PRAKASHAN</p>
                <a href="https://drive.google.com/file/d/1dtmZ995DCO-JmEagCnf0No9Qlu4F129e/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/inorganic.webp")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">INORGANIC CHEMISTRY</h5>
                <p>NIRALI PRAKASHAN</p>
                <a href="https://drive.google.com/file/d/1e9nXu8hLd0Y75sAzR2uF45rtV0kvSz9-/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/remedialBio.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">REMEDIAL BIOLOGY</h5>
                <p>NIRALI PRAKASHAN</p>
                <a href="https://drive.google.com/file/d/1eAuae42LPBEV1uE0NGgvtbg34VTMi_nQ/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/remedialMaths.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">REMEDIAL MATHS</h5>
                <p>NIRALI PRAKASHAN</p>
                <a href="https://drive.google.com/file/d/1eBOM8AQnCi1F1LdFBPr7dUX663fb1FlS/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/communication.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">COMMUNICATION SKILLS</h5>
                <p>CAREWELL PHARMA</p>
                <a href="https://drive.google.com/file/d/1E0jB72Xfs7UwXpxIlzJVCOBRp01XTXBE/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>
        </div>
         
        </div>
        <hr/>

        <div>
        <h4>JOIN OUR TELEGRAM GROUP FOR MORE PHARMACY NOTES</h4>
        <div class="socials mb-5"><a href="https://www.github.com/Sharath1036/"><img alt="image" class="icons" src={require("../images/telegram.webp")} /></a></div>
        </div>
        <div ><Footer /></div>
        </div>
    )
}