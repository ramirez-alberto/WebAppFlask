import { Album } from "./album.model";

export interface Cancion {
  id : number;
  titulo : string;
  minutos : number;
  segundos : number;
  interprete : string;

  albumes?: Album[];
}
