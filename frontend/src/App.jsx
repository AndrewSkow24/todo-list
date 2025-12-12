import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import AddTask from "./components/AddTask";
import TotoList from "./components/TotoList";
import Login from "./components/Login";
import SignUp from "./components/SignUp";
import { Nav, Navbar } from "react-bootstrap";
import Container from "react-bootstrap/Navbar";

function App() {
  let user = "True";

  return (
    <div className="App">
      <Navbar bg="primary" variant="dark">
        <div className="container-fluid">
          <Navbar.Brand>Список задач</Navbar.Brand>
          <Nav className="me-auto">
            <Container>
              <Link className="nav-link" to="/tasks">
                Список задач
              </Link>
              {user ? (
                <Link className="nav-link">Выйти ({user})</Link>
              ) : (
                <>
                  <Link className="nav-link" to={"/login"}>
                    Войти
                  </Link>
                  <Link className="nav-link" to={"/signup"}>
                    Регистрация
                  </Link>
                </>
              )}
            </Container>
          </Nav>
        </div>
      </Navbar>
    </div>
  );
}

export default App;
