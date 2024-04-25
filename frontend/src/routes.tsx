import {
  createBrowserRouter,
} from "react-router-dom";

import Todo from './components/Todo/Todo.tsx';
import EditTodo from './components/Todo/EditTodo/EditTodo.tsx';

const router = createBrowserRouter([
  {
    path: "/",
    element: <Todo />,
  },
  {
    path: "/edit/:id",
    element: <EditTodo />,
  },
]);

export default router