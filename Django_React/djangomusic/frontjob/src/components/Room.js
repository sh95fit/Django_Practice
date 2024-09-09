import React, { Component } from "react";
import { useParams } from 'react-router-dom';

export default class Room extends Component{
  constructor(props) {
    super(props);
    this.state = {
      votesToSkip: 1,
      guestCanPause: false,
      isHost:false,
    };
    // this.roomTitle = this.props.match.params.roomTitle; (v6에서는 사용할 수 없음! v5에서 사용하는 형태)
  }

  componentDidMount() {
    this.getRoomDetails();
  }

  getRoomDetails() {
    const { roomTitle } = this.props;
    fetch(`/musicapi/get?title=${roomTitle}`).then((response) => response.json()).then((data) => {
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


  render() {
    const { roomTitle } = this.props;
    const { votesToSkip, guestCanPause, isHost } = this.state;

    // 상태가 초기화되기 전에 렌더링을 방지
    // if (votesToSkip === undefined || guestCanPause === undefined || isHost === undefined) {
    //   return <div>Loading...</div>;
    // }

    return(<div>
      <h3>{ roomTitle }</h3>
      <p>투표 : {this.state.votesToSkip}</p>
      <p>방문자 권한 : {guestCanPause !== undefined ? guestCanPause.toString() : '정보 없음'}</p>
      <p>호스트 : {isHost !== undefined ? isHost.toString() : '정보 없음'}</p>
    </div>);
  }

}