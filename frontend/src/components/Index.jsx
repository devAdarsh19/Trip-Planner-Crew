import React from "react";
import { Link } from "react-router-dom";

const Index = () => {

  const handlePlanning = () => {
    Link("/plan-trip");
  };

  return (
    <div>
      <div className="min-h-screen flex flex-col items-center justify-center p-6 bg-gradient-to-r from-blue-100 to-indigo-200">
        <h1 className="text-5xl font-bold mb-6 text-center">
          Welcome to Trip Planner Crew
        </h1>
        <p className="text-lg mb-8 text-center max-w-xl">
          Your AI-powered assistant to help you generate a perfect 7-day
          itinerary tailored to your location, destination, travel dates, and
          interests.
        </p>
        <button
          onClick={handlePlanning}
          size="lg"
          className="text-lg px-8 py-4"
        >
          Start Planning Your Trip
        </button>
      </div>
    </div>
  );
};

export default Index;
