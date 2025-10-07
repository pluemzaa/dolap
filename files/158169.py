<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3591;&#3634;&#3609; 3"/>
        <attribute name="authors" value="DR-R22A8-49SS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 10:54:21 PM"/>
        <attribute name="created" value="RFItUjIyQTgtNDlTUztEUi1SMjJSQTgtNDlTUzsyNTY4LTA3LTIxOzEwOjQxOjU2IFBNOzMwMTA="/>
        <attribute name="edited" value="RFItUjIyQTgtNDlTUztEUi1SMjJSQTgtNDlTUzsyNTY4LTA3LTIxOzEwOjU0OjIxIFBNOzQ7MzExNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="num, end" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="num"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="end"/>
            <if expression="num &lt; 7">
                <then>
                    <for variable="num" start="num" end="end" direction="inc" step="1">
                        <output expression="num" newline="True"/>
                    </for>
                </then>
                <else/>
            </if>
        </body>
    </function>
</flowgorithm>