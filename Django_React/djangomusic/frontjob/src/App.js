import React, { Component } from "react";
import Home from "./components/Home";

export default class App extends Component{
  constructor(props) {
    super(props);
  }

  render() {
    // return <h1> {this.props.hello} 연동 화면입니다.</h1>
    return (
      <div>
        <Home/>
      </div>
    )
  }
}

// React 18에 맞는 createRoot 사용  (index.js로 이동)
// const appDiv = document.getElementById("app");
// const root = createRoot(appDiv);  // createRoot로 root 생성
// root.render(<App />);  // root에 App 렌더링