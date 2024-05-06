import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

export const firebaseConfig = {
  apiKey: "AIzaSyCSLahcsBeiilPoGXQAR-qIN-qG_l6a_Ik",
  authDomain: "hackfestismdhn.firebaseapp.com",
  projectId: "hackfestismdhn",
  storageBucket: "hackfestismdhn.appspot.com",
  messagingSenderId: "876446756332",
  appId: "1:876446756332:web:0866b0005dd78d847124c9",
  measurementId: "G-W7J0XMXBK2"
};

initializeApp(firebaseConfig);
export const auth = getAuth();