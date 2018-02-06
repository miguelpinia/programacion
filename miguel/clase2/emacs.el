;;; python.el --- Summary
;;; Commentary:
;; Configuración básica para usar Emacs como editor predeterminado de
;; python.
;;
;;; Code:
(require 'package)

;; Descripción de repositorios.
(add-to-list 'package-archives
             '("marmalade" . "http://marmalade-repo.org/packages/") t)
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)
(add-to-list 'package-archives
             '("org" . "http://orgmode.org/elpa/") t)

(package-initialize)

(when (not package-archive-contents)
  (package-refresh-contents)) ;; C-x C-e, evaluar código lisp

;; Función de ayuda. Instala paquetes si no han sido instalados.
(defun install-if-needed (package)
  "Instala un paquete para emacs si es necesario"
  (unless (package-installed-p package)
    (package-install package)))

;; Paquetes que necesitamos instalar en emacs.
(defvar my-packages
  '(material-theme
    flycheck
    py-autopep8
    magit
    yasnippet
    jedi
    auto-complete
    autopair
    projectile
    helm))

;; Instala los paquetes previos.
(mapc 'install-if-needed my-packages)

;; Usamos autocompletado.
(require 'auto-complete)
;; Las reglas de buena escritura de código.
(require 'py-autopep8)
;; Pareamiento automático de paréntesis y otros.
(require 'autopair)
;; Snippets de código.
(require 'yasnippet)
;; Validación de código.
(require 'flycheck)
;; Herramientas para trabajar con python dinámicamente
(require 'jedi)
(require 'helm)

;;;;;;;;;;;;;;;;;;;;
;; Configuración. ;;
;;;;;;;;;;;;;;;;;;;;
(load-theme 'material t)

(global-flycheck-mode t)


(add-to-list 'ac-dictionary-directories "~/.emacs.d/custom/dict")
(setq yas-snippet-dirs '("~/.emacs.d/snippets"))
(global-set-key "\C-xg" 'magit-status)
(setq
 ac-auto-start 2
 ac-override-local-map nil
 ac-use-menu-map t
 ac-candidate-limit 20)

(add-to-list 'auto-mode-alist '("\\.py$" . python-mode))
(setq py-electric-colon-active t)
(add-hook 'python-mode-hook 'autopair-mode)
(add-hook 'python-mode-hook 'yas-minor-mode)

(add-hook 'python-mode-hook
	  (lambda ()
	    (linum-mode 0)
	    (jedi:setup)
	    (jedi:ac-setup)
            (local-set-key "\C-cd" 'jedi:show-doc)
            (local-set-key (kbd "M-SPC") 'jedi:complete)
            (local-set-key (kbd "M-.") 'jedi:goto-definition)))

(add-hook 'python-mode-hook 'auto-complete-mode)
(add-hook 'inferior-python-mode-hook (lambda ()
                                       (linum-mode 0)))
(add-hook 'python-mode-hook 'py-autopep8-enable-on-save)
(setq py-autopep8-options '("--max-line-length=100"))
(setq py-autopep8-options '("--inplace"))
(setq py-autopep8-options '("--aggressive"))
(setq py-autopep8-options '("--aggressive"))
(setq jedi:complete-on-dot t)
(ido-mode t)
(windmove-default-keybindings 'shift)
(show-paren-mode t)
(setq visible-bell nil)

(global-set-key (kbd "C-c h") 'helm-command-prefix)
(global-set-key (kbd "M-x") 'helm-M-x)
(global-set-key (kbd "C-x C-f") 'helm-find-files)
(define-key helm-map (kbd "<tab>") 'helm-execute-persistent-action)
(define-key helm-map (kbd "C-i") 'helm-execute-persistent-action)
(define-key helm-map (kbd "C-z")  'helm-select-action)
(when (executable-find "curl")
  (setq helm-net-prefer-curl t))
(setq helm-split-window-in-side-p           t
      helm-move-to-line-cycle-in-source     t
      helm-ff-search-library-in-sexp        t
      helm-scroll-amount                    8
      helm-ff-file-name-history-use-recentf t)
(helm-mode 1)
(setq helm-M-x-fuzzy-match t)
(global-set-key (kbd "M-y") 'helm-show-kill-ring)
(global-set-key (kbd "C-x b") 'helm-mini)
(setq helm-buffers-fuzzy-matching t
      helm-recentf-fuzzy-match    t)

;;; python.el ends here
