<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Lab4_3"/>
        <attribute name="authors" value="bizr"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 12:29:36 "/>
        <attribute name="created" value="Yml6cjtNQUNCT09LQUlSOzI1NjgtMDctMjA7IjEyOjIyOjIxICI7MjM2Mg=="/>
        <attribute name="edited" value="Yml6cjtNQUNCT09LQUlSOzI1NjgtMDctMjA7IjEyOjI5OjM2ICI7MTsyNDgz"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Integer" array="False" size=""/>
            <output expression="&quot;Input start number:&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number:&quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i&lt;=n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>