

tmux notes:

* detach from session/pane: `ctrl-b` then `d`
* attach to session/pane (if you only have one session running): `tmux attach`
* list tmux sessions: `tmux ls`
* pretty print tmux sessions with pid:  `tmux list-panes -F '#{pane_active} #{pane_pid}'`


Ok, this is kind of all we need:
https://gist.github.com/willfurnass/19588766e3f0145a49e4b3a38ec0801c


* `tmux new -s session_name` - creates a new tmux session named session_name
* `tmux attach -t session_name` - attach to that specific tmux session
