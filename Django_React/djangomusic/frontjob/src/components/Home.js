import React, { Component } from "react";

import RoomJoinPage from "./RoomJoinPage";
import NewMakeRoomPage from "./NewMakeRoomPage";

import {BrowserRouter as Router, Route, Routes, Link, Navigate} from "react-router-dom";

export default class Home extends Component{
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<h1>홈페이지입니다.</h1>}></Route>
          <Route path="/join" element={<RoomJoinPage/>}></Route>
          <Route path="/create" element={<NewMakeRoomPage/>}></Route>
        </Routes>
      </Router>
    )
  }

}