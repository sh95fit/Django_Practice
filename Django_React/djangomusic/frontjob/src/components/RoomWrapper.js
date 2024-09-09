import React from 'react';
import { useParams } from 'react-router-dom';
import Room from './Room';

const RoomWrapper = () => {
  const { roomTitle } = useParams(); // URL 파라미터 가져오기
  return <Room roomTitle={roomTitle} />;
};

export default RoomWrapper;