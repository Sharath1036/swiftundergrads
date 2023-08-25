import React from 'react';
import "../App.css";
import "../responsive.css";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function Contact() {

  return (
    <div>
      <div class="container-fluid bg7">
        <Navbar />
        <br /><br /><br /><br /><br /><br /><br/><br/>
        <div class="jumbotron bg-transparent align-items-center mx-auto d-block">
          <h1 align="center" class="text-white">Contact Page</h1>
        </div>
      </div>

      <div class="container mb-5">
        <h2 class="mt-5">Contact Us</h2>
        <p>Fill out the form so that we can reach out to you...</p>
        <form class="needs-validation" novalidate>

          <div class="row">
          <div class="col-lg-6">
          <div class="form-group">
            <label for="fname">First Name:</label>
            <input type="text" class="form-control" id="fname" placeholder="Enter Name" name="fname" pattern="[A-Za-z]{1,20}"  required/>
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>
          </div>

          <div class="col-lg-6">
          <div class="form-group">
            <label for="lname">Last Name:</label>
            <input type="text" class="form-control" id="lname" placeholder="Enter Surname" name="lname" pattern="[A-Za-z]{1,20}" required/>
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>
          </div>
          </div>

          <div class="form-group">
            <label for="email">Email ID:</label>
            <input type="email" class="form-control" id="email" placeholder="Enter Email ID" name="email" required />
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <div class="form-group">
            <label for="contact">Contact Number:</label>
            <input type="text" class="form-control" id="contactno" placeholder="Enter Contact Number" name="contact" pattern="[6-9]{1}[0-9]{9}" required />
            <div class="valid-feedback">Valid.</div>
            <div class="invalid-feedback">Invalid Contact Number.</div>
          </div>

          <div class="form-group">
            <label for="comment">Reason for contacting:</label>
            <textarea class="form-control" rows="5" id="comment" name="comment" required></textarea>
          </div> 

          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
      <div class="mgn"><Footer /></div>
    </div>
  );
}
