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
                <a href="https://drive.google.com/file/d/1GHImp8K43V72PL0D0P4K3hwYQbiIkZBV/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/avadhanulu.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING PHYSICS</h5>
                <p>M.N. AVADHANULU</p>
                <a href="https://drive.google.com/file/d/1T-jGVlZALNEfaCN2ZmbM1rtTfdC26JWa/view?usp=sharing" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/jainjain.jpeg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING CHEMISTRY</h5>
                <p>JAIN & JAIN</p>
                <a href="https://drive.google.com/file/d/1S00JxPqeMWBTjRNa0ygpk05VGdyTDNiX/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/hughes.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">BASIC ELECTRICAL ENGINEERING</h5>
                <p>EDWARD HUGHES</p>
                <a href="https://drive.google.com/file/d/17lH8WjcOglTw2zYy43ORn1DLlVrIJoRt/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/bxe.png")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">BASIC ELECTRONICS ENGG</h5>
                <p>PUNE UNIVERSITY</p>
                <a href="https://drive.google.com/file/d/1fvXLpEVn4PBb9u_EGtL2dDKz6x5DTp7L/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/hibbeler.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING MECHANICS</h5>
                <p>R.C. HIBBELER</p>
                <a href="https://drive.google.com/file/d/16clLtahhrKZc6PP1Hi18wo3B5mOrtkJY/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/bhatt.png")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">ENGINEERING DRAWING</h5>
                <p>N.D. BHATT</p>
                <a href="https://drive.google.com/file/d/1u2Pv2Jwfx2jYUVjGZXlizPmgj_wlQcv4/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/letUsC.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">LET US C</h5>
                <p>YASHAVANT KANETKAR</p>
                <a href="https://drive.google.com/file/d/1wcJDaIzLT0nM8XAQNaM_0xlOX1UhjDvN/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/communication.jpg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">COMMUNICATION SKILLS</h5>
                <p>SHIRLEY MATHEW</p>
                <a href="https://drive.google.com/file/d/1yEnkhFMvI3Gqy2eMiKJybv3L-yzbxx0L/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>

          <div class="col-lg-4">
            <div class="card mb-5 shadow">
            <img class="card-img-top" height="450" src={require("../images/pythonBook.jpeg")} alt="Card image" />
              <div class="card-body">
                <h5 class="card-title">PYTHON PROGRAMMING</h5>
                <p>MALLA REDDY COLLEGE</p>
                <a href="https://drive.google.com/file/d/1gAb6ouZO_hFtgfSBY6Z-f2UruXhddcLo/view?usp=drive_link" target="_blank" class="btn w-100 btn-danger">VIEW PDF</a>
              </div>
            </div>
          </div>




        </div>
        </div>
      
        <div ><Footer /></div>
        </div>
    )
}