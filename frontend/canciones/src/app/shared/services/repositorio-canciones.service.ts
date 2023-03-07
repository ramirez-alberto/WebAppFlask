import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { EnvironmentUrlService } from './environment-url.service';
import { Cancion } from 'src/app/_interfaces/cancion.model';

@Injectable({
  providedIn: 'root'
})
export class RepositorioCancionesService {

  constructor(private envUrl: EnvironmentUrlService, private http: HttpClient) { }

  public getCanciones = (route : string) => {
    return this.http.get<Cancion[]>(this.createRoute(route, this.envUrl.urlAddress))
  }

  private createRoute = (route : string, envAddress : string) =>{
    return `${envAddress}/${route}`
  }
}
