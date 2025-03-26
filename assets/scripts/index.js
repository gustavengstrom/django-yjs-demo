
import { Editor } from '@tiptap/core'
import StarterKit from '@tiptap/starter-kit'
import { WebsocketProvider } from 'y-websocket'
import Collaboration from '@tiptap/extension-collaboration'
import CollaborationCursor from '@tiptap/extension-collaboration-cursor'
import * as Y from 'yjs' 

// export { Editor }; 
// export { StarterKit }; 
// export { HocuspocusProvider }; 
// export { WebsocketProvider }; 
// export { Collaboration }; 
// export { CollaborationCursor }; 
// export { Y }; 

// import into the window scope
window.Editor = Editor;
window.StarterKit = StarterKit;
window.Y = Y;
window.WebsocketProvider = WebsocketProvider;
window.Collaboration = Collaboration;
window.CollaborationCursor = CollaborationCursor;
// window.WebsocketProvider = WebsocketProvider;
console.log("HEJ INDEX")