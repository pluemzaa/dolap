<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work_flowforithm_2"/>
        <attribute name="authors" value="Vivobook"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:20:32 PM"/>
        <attribute name="created" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDY6MTI6MjkgUE07MzE3NA=="/>
        <attribute name="edited" value="Vml2b2Jvb2s7TEFQVE9QLTFEODVNVU02OzI1NjgtMDctMTY7MDY6MjA6MzIgUE07MTszMjc1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="i, n" type="Real" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="n"/>
            <while expression="i &lt;= n">
                <output expression="i" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>