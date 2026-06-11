<?php

namespace App\Http\Controllers;

use App\Models\Writer;
use Illuminate\Http\Request;

class WriterController extends Controller
{
    /**
     * отобразить список писателей
     */
    public function index()
    {
        $writers = Writer::all();
        return view("writers.index", compact("writers"));
    }
}
