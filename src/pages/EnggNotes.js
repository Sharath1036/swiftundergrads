import React from 'react';
import '../App.css';
import "../responsive.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function EnggNotes () {
    return(
        <div class="App">
      <div class="container-fluid bg5">
        <Navbar />
        <br /><br /><br /><br /><br /><br />
        <div class="jumbotron bg-transparent align-items-center mx-auto d-block">
          <h1>Engineering Notes</h1>
        </div>
        </div>
        <br /><br /><br />
        <div class="container-fluid">
        <div class="row">
          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/bsgrewal.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING MATHEMATICS</h5>
                <p>B.S. GREWAL</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/avadhanulu.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING PHYSICS</h5>
                <p>M.N. AVADHANULU</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/jainjain.jpeg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING CHEMISTRY</h5>
                <p>JAIN & JAIN</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/hughes.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">BASIC ELECTRICAL ENGINEERING</h5>
                <p>EDWARD HUGHES</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/bxe.png")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">BASIC ELECTRONICS ENGG</h5>
                <p>PUNE UNIVERSITY</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/hibbeler.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING MECHANICS</h5>
                <p>R.C. HIBBELER</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/bhatt.png")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING DRAWING</h5>
                <p>N.D. BHATT</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/letUsC.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">LET US C</h5>
                <p>YASHAVANT KANETKAR</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/communication.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">COMMUNICATION SKILLS</h5>
                <p>SHIRLEY MATHEW</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/pythonBook.jpeg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">PYTHON PROGRAMMING</h5>
                <p>MALLA REDDY COLLEGE</p>
                <a href="#" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>




        </div>
        </div>
      
        <div ><Footer /></div>
        </div>
    )
}