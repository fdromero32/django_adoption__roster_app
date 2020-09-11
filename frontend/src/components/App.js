import React, { Component } from "react";
import { render } from "react-dom";


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading...",
    };
  }

  componentDidMount() {
    fetch("api/adoption")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <React.Fragment>
        <div className="table-style">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Species</th>
              <th>Breed</th>
              <th>Age</th>
              <th>Description</th>
            </tr>
          </thead>
          <tbody>
            {this.state.data.map((pet) => {
              return (
                <tr key={pet.id}>
                  <td>{pet.name}</td>
                  <td>{pet.species}</td>
                  <td>{pet.breed}</td>
                  <td>{pet.age}</td>
                  <td>{pet.description}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
        </div>
      </React.Fragment>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
