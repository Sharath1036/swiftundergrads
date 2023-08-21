import React from "react";
import  '../App.css';
import "../responsive.css";

const Service = (props) => {   
    console.log(props);
    return(
        <div class="container mb-5">
        <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
          <ol class="carousel-indicators">
            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
          </ol>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img class="d-block w-100" src={require("../images/notes.jpg")} alt="First slide"/>
              <div class="carousel-caption d-none d-md-block">
                <h5>Notes</h5>
              </div>
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src={require("../images/mocks.jpg")} alt="Second slide"/>
              <div class="carousel-caption d-none d-md-block">
                <h5>Mock Tests</h5>
              </div>
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src={require("../images/webinars.jpg")} alt="Third slide"/>
              <div class="carousel-caption d-none d-md-block">
                <h5>Webinars</h5>
              </div>
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src={require("../images/guidance.jpg")} alt="Third slide"/>
              <div class="carousel-caption d-none d-md-block">
                <h5>Admission Procedure Guidance</h5>
              </div>
            </div>
          </div>
          <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="sr-only">Previous</span>
          </a>
          <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="sr-only">Next</span>
          </a>
        </div>
      
      </div> 
)
} 

export default Service;