<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3588;&#3619;&#3633;&#3657;&#3591;&#3607;&#3637;&#3656; 1 &#3586;&#3657;&#3629; 3"/>
        <attribute name="authors" value="tpath"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 10:40:06 PM"/>
        <attribute name="created" value="dHBhdGg7Tk9QOzIwMjUtMDctMTY7MTA6MTk6MTggUE07MjA2OQ=="/>
        <attribute name="edited" value="dHBhdGg7Tk9QOzIwMjUtMDctMTY7MTA6NDA6MDYgUE07MTsyMTY4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="n, b" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="n"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="b"/>
            <while expression="n &lt;= b">
                <output expression="n" newline="True"/>
                <assign variable="n" expression="n+1"/>
            </while>
        </body>
    </function>
</flowgorithm>