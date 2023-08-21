import React from "react";
import "../App.css";
import "../responsive.css";
import prathamesh from "../images/prathamesh.jpg";
import omkar from "../images/omkar.jpg";

export default function Testimonials() {
  const data = [
    {
      id: 1,
      image: omkar,
      title: "Messiahs!",
      description: "I had lost hopes due to my low score. But Swift UnderGrads came in at the right time and helped me to get admission!",
      name: "OMKAR SHINDE",
      college: "P.G. COLLEGE OF PHARMACEUTICAL SCIENCE AND RESEARCH",
    },

    {
      id: 2,
      image: prathamesh,
      title: "Amazing experience",
      description: "It was quite a great experience with Swift UnderGrads which was much better than other paid guidance. Due to their team, I got admission in government college and I am enjoying my college life!",
      name: "PRATHAMESH BANNE",
      college: "GOVERNMENT COLLEGE OF ENGINEERING, AMRAVATI",
    },
       
  ];

  const mapFunction = data.map((item, pos) => {
    console.log(item);

    return (
      <div class="card mb-5 shadow mx-auto d-block text-center brdr">
        <div class="card-item">
        <img class="rounded-circle mt-5 mb-3" src={item.image} width="150" height="150" />
        <h5 class="card-name m-0">{item.title}</h5>
        <img class="mt-4" src={require("../images/double-quote-bottom.png")} width="10%" height="10%" />
        <p class="text-dark card-text m-3">{item.description}</p>  
        <h3 class="m-3">{item.name}</h3>
        <p class="text-dark txt-clg">{item.college}</p>
        </div>
      </div>
    );
  });

  return <div class="App">{mapFunction}</div>;
}
