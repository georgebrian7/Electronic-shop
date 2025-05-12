import { Outlet, useParams } from "react-router-dom";
import DefaultProfile from "./Landing";
import Cart from "./Cart"
const Profile = () => {
    const {name} =useParams()
    return (
      <div>
        <h1>Hello from profile page!</h1>
        <p>So, how are you?</p>
        <h2>The profile visited is here</h2>
        {name === "cart" ?(
            <Cart/>
        ) : (
         <DefaultProfile/>   
        )}
      </div>
    );
  };
  
  export default Profile;