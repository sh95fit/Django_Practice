import React, { Component } from "react";
import { useParams } from 'react-router-dom';

import { Button, Grid, Typography } from "@mui/material";

import { Link } from "react-router-dom";

import { useNavigate } from 'react-router-dom';

import CreateRoomPage from "./NewMakeRoomPage";

// HOC를 이용해 navigate를 props로 전달
function withRouter(Component) {
  function ComponentWithRouterProp(props) {
    const navigate = useNavigate();
    return <Component {...props} navigate={navigate} />;
  }

  return ComponentWithRouterProp;
}



class Room extends Component{
  constructor(props) {
    super(props);
    this.state = {
      votesToSkip: 1,
      guestCanPause: false,
      isHost:false,
      showSettings:false,
    };
    // this.roomTitle = this.props.match.params.roomTitle; (v6에서는 사용할 수 없음! v5에서 사용하는 형태)
    this.leaveButtonPressed= this.leaveButtonPressed.bind(this);
    this.updateShowSettings= this.updateShowSettings.bind(this);
    this.renderSettingsButton = this.renderSettingsButton.bind(this);
    this.renderSettings = this.renderSettings.bind(this);
  }

  componentDidMount() {
    this.getRoomDetails();
  }

  getRoomDetails() {
    const { roomTitle } = this.props;
    fetch(`/musicapi/get?title=${roomTitle}`).then((response) => {
      if (!response.ok) {
        this.props.leaveRoomCallback();
        this.props.navigate("/");
      }
      return response.json();
    }).then((data) => {
      this.setState({
        votesToSkip: data.vote_to_skip,
        guestCanPause: data.guest_can_pause,
        isHost: data.is_host,
      });
    })
    .catch((error) => {
      console.error('Error fetching room details:', error);
    });
  }

  leaveButtonPressed() {
    const requestOptions = {
      method: "POST",
      headers: {"Content-Type":"application/json"},
    };
    fetch("/musicapi/leave", requestOptions).then((_response) => {
      this.props.leaveRoomCallback();
      this.props.navigate("/");
    })
  }

  updateShowSettings(value){
    this.setState({
      showSettings: value,
    });
  }

  renderSettingsButton() {
    return (
      <Grid item xs={12} align="center">
        <Button
          variant="contained"
          color="primary"
          onClick={() => this.updateShowSettings(true)}
        >Settings</Button>
      </Grid>
    )
  }

  renderSettings() {
    return (
      <Grid container spacing={1}>
        <Grid item xs={12} align="center">
          <CreateRoomPage
            update={true}
            votesToSkip={this.state.votesToSkip}
            guestCanPause={this.state.guestCanPause}
            roomTitle={this.roomTitle}
            updateCallback={() => { }}
          />
        </Grid>
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={() => this.updateShowSettings(false)}
          >
            닫기
          </Button>
        </Grid>
      </Grid>
    );
  }


  render() {
    const { roomTitle } = this.props;
    const { votesToSkip, guestCanPause, isHost } = this.state;

    if (this.state.showSettings) {
      return this.renderSettings();
    }
    return(
      <Grid container spacing = {1}>
        <Grid item xs={12} align="center">
          <Typography variant="h4" component="h4">
            Room Code : { roomTitle }
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            투표 : {this.state.votesToSkip}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            방문자 권한 : {guestCanPause !== undefined ? guestCanPause.toString() : '정보 없음'}
          </Typography>
        </Grid>
        <Grid item xs={12} align="center">
          <Typography variant="h6" component="h6">
            호스트 : {isHost !== undefined ? isHost.toString() : '정보 없음'}
          </Typography>
        </Grid>
        {this.state.isHost ? this.renderSettingsButton() : null}
        <Grid item xs={12} align="center">
          <Button
            variant="contained"
            color="secondary"
            onClick={this.leaveButtonPressed}
          >방 나가기</Button>
        </Grid>
      </Grid>
    )
    // 상태가 초기화되기 전에 렌더링을 방지
    // if (votesToSkip === undefined || guestCanPause === undefined || isHost === undefined) {
    //   return <div>Loading...</div>;
    // }

    // return(<div>
    //   <h3>{ roomTitle }</h3>
    //   <p>투표 : {this.state.votesToSkip}</p>
    //   <p>방문자 권한 : {guestCanPause !== undefined ? guestCanPause.toString() : '정보 없음'}</p>
    //   <p>호스트 : {isHost !== undefined ? isHost.toString() : '정보 없음'}</p>
    // </div>);
  }
}

export default withRouter(Room);